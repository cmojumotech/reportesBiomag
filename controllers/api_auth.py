import json
import requests
from odoo import http
from odoo.http import request

class APIAuthController(http.Controller):

    @http.route('/api_auth/test', type='http', auth='public', methods=['GET'], csrf=False)
    def test_api_auth(self, **kwargs):
        # Utilizamos el Access Token proporcionado para hacer una petición de prueba
        access_token = 'sl.u.AFngFZVC09lv-nv9YRUhh_maQ8gVDtwhzgM9ugB6estvL2o8nUdYjq4kuSz_oIZdbfdTR9xSCgQzCPYEP5mNqskPzGQcRN0RsYu9koj3wEkAdXdrCZS9tQ2TVRL8S6vugB19sNq2P-W9mHeaeIze203zP0Pe3K_42G30JqJoAgD1SOrFPleoydmngVe-MmY_tHQ9TDxFOFz4ywAH4ImwZI9P2_QsdsScUKdpMBLoi4FHIoj4e77FtIK2Y7sPO1tNpThivKUIlYL5IpeDPB2tnyZmpUoCLDi4yo_KQlAVMSyaR5_8jq1OqcTQvicG4wBCIbhNzP_3vNLZObLVOlh0l_O5YGMYwYEMWQqu7T93wres-7_VfvA6JzsRyuM5A3LP20pPg9rkjpXCcYST-7acAIBilpBmdccZv6LGMZFVoz8CkWwJqJqaKD77-uPkH0h7HENh7PtZTF9_t-0-fiCa88IG89-WWeqiFD94dM-7dCcUF1NYls5_9v4MbGm5-UU3HPrFlFpjEfSO4018Vim3KoCQSqfMZZmvmRAd3hzz8QQjcfKHVGdNPNczNSB41M7rwYaEztY1MzAMf8qXTa8uqLMF9gowpVPwGhUAc3Ul6M1xGEeC80ykfgaatUMvw4tjJInpoPVuCr0XnciF82Kz9qmoZEoB1RaWoY87AFqokXYuCNiQWQJhlYW8v4dLgNr-E_mr0--eULEJKPV8GEyTnEHEUHG_7yIAtQ1Ue27xK9dT49MwURBYa_TQBPHtiHBamziqfb9mXNhGj1G1TS9U3lBgE9MukyORHpzpgFZSJuj7xJBFIuSYBhPIw94Ke2qEzx-ah5GwFqM_s5GQdIZTA3xOJCYmBhRFcKbZsOe1nUQ2zE4UmHsAb-ACwNwCMvsPTxuqXdVEMg_v48wSKL0K3fCgM_skkfPMZmFLWwBN4ZyVTvAGDjYJedySbAUKQUEPfkMHzEreBDu2fnvKJ6FUNOhmhW-peQDIWhlteIwKi28cEf-63OYiEIuliJnxk8eXsL-tc02Z39IvvM2gZS34gRUnoWHFb7cMPTT1XMX-W__dI7XEK5fDQMFUSFI5IUtS4mpdnDXYP8Xwg2PYuR6JG2p60J4MFx_uo8sxOQ8whbAExOTOze8ZsTDO5grvEwHhAbYokptA1YfVzWNv9Zmpo1J8BqkBr9uSEMcX0i7CxX7Mq_NjDavArAL412r4bdtV1-bPclxh3D4irtF8dkixe8UArmBySoCuNdQ8iadeL4z_YCc8vCArFrtvVhehFjIryN1j_ygHm3Z13Xox-HpkExNB_Hc-bhKfq9Ty1FUm0fqcugXgemOPop6mojerD8KrLP6gHwrjipVaj0KVCh3cxfI1fNIA8esmQxcUiF7d1ZtT3BtxsWWQePj133uGwXr2-NbYRVPHVSrf4lFh_L8WvDa-UDM2tjSrCSaHOv5M3-7hDmmxXcf-dUVgeaTZlWWcFjOj591wMx7bhOoC1H74UBHY'
        headers = {'Authorization': 'Bearer %s' % access_token}
        
        # URL de ejemplo de la API externa (modifica a la real)
        api_url = 'https://api.example.com/data'
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return request.make_response(json.dumps(data), headers=[('Content-Type', 'application/json')])
        else:
            # Aquí iría la lógica para renovar el token usando el Refresh Token, según la documentación de la API
            return request.make_response(json.dumps({'error': 'Error en la llamada a la API externa'}), status=400, headers=[('Content-Type', 'application/json')])