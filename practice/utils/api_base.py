from playwright.sync_api import Playwright, APIResponse

orders_payload = {'orders': [{'country': 'India', 'productOrderedId': '6581ca399fd99c85e8ee7f45'}]}
class APIUtils:

    def generate_token(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('/api/ecom/auth/login',
                                            data={'userEmail': 'rahulshetty@gmail.com',
                                                  'userPassword': 'iamking@000'})
        assert response.ok
        response_json = response.json()
        token = response_json['token']
        return token

    def create_order(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('/api/ecom/order/create-order', data=orders_payload,
                                 headers={'Authorization': self.generate_token(playwright),
                                          'Content-type': 'application/json'})
        return response.json()['order'][0]
