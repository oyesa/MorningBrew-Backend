import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
       
        errors = data.get('errors', None)

        if errors is not None:
           
            return super(UserJSONRenderer, self).render(data)


        # Finally, we can render our data under the "user" namespace.
        return json.dumps({
            'CustomUser': data
        })