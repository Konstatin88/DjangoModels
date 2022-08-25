from django import template

register = template.Library()


SAFE_WORDS = ('ни', 'пи' )


@register.filter()
def censor(text):
   if not isinstance(text,str):
      raise ValueError('Цензор применяеться только к строке')

   text = text.split()
   for n, w in enumerate(text):
      if w.lower().startswith(SAFE_WORDS):
         cen = '**' + w[2:]
         text[n] = cen
   text = ' '.join(text)



   return f'{text}'