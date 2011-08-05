from __future__ import print_function
from django import template
from django.conf import settings
import popen2
import re

register = template.Library()

class PhpNode(template.Node):
    _tags = ('$$django(<)php$$?', '?$$django(>)php$$')

    def __init__(self, code):
        self._code = code

    def render(self, context):
        return self._code.join(self._tags)

class StartphpNode(PhpNode):
    def __init__(self, nodelist):
        self._nodelist = nodelist

    def render(self, context):
        self._code = 'php ' + self._nodelist.render(context)
        return super(StartphpNode, self).render(context)

@register.tag
def php(parser, token):
    '''{% php echo 9; %}'''
    return PhpNode(token.contents)

@register.tag
def startphp(parser, token):
    '''{% startphp %}echo 9;{% endphp %}'''
    nodelist = parser.parse(['endphp'])
    parser.delete_first_token()
    return StartphpNode(nodelist)

_binary = getattr(settings, 'PHP_CGI', 'php-cgi') + ' -q'

def _preprocess(s):
    output, input = popen2.popen2(_binary)
    print(s, end='', file=input)
    input.close()
    return output.read()

_remove_php = re.compile('(<(?=[?])|(?<=[?])>)')

def _replace_render(f):
    def _f(self, context):
        s = (_remove_php.sub(r'##django(\1)php##', f(self, context))
            .replace('$$django(<)php$$', '<').replace('$$django(>)php$$', '>'))
        s = (_preprocess(s)
            .replace('##django(<)php##', '<').replace('##django(>)php##', '>'))
        return s
    return _f

template.Template.render = _replace_render(template.Template.render)
