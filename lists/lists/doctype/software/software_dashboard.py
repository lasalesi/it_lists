from frappe import _

def get_data():
   return {
      'fieldname': 'software',
      'transactions': [
         {
            'label': _('Related documents'),
            'items': ['Software assessment']
         }
      ]
   }
