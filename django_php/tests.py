from django.template import Template, Context
from django.test import TestCase
from django_php.templatetags.php import php, startphp

def render_template(template, **kwargs):
    return Template(template).render(Context(**kwargs))

class PhpTest(TestCase):
    def test_php(self):
        s = render_template('{% load php %}' + php.__doc__)
        self.assertEqual(s, '9')

    def test_startphp(self):
        s = render_template('{% load php %}' + startphp.__doc__)
        self.assertEqual(s, '9')

    def test_php_tags(self):
        s = render_template('{% load php %}<?php echo 9;?>')
        self.assertEqual(s, '<?php echo 9;?>')
