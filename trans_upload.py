import json
import os
from tqdm import tqdm

from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service

ori_outputs = "ori_outputs"
def get_csvs(filepath):
    ret = []
    if os.path.exists(filepath):
        f = open(filepath, "r")
        for line in f:
            ret.append(line.strip())
        f.close()
    return ret


ak = ""
sk = ""

k_access_key = ak  # https://console.volcengine.com/iam/keymanage/
k_secret_key = sk
k_service_info = \
    ServiceInfo('open.volcengineapi.com',
                {'Content-Type': 'application/json'},
                Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
                5,
                5)
k_query = {
    'Action': 'TranslateText',
    'Version': '2020-06-01'
}
k_api_info = {
    'translate': ApiInfo('POST', '/', k_query, {}, {})
}
service = Service(k_service_info, k_api_info)

for target_language in ["zh", "de", "lv", "ja", "ko", "pt"]:
    for txt_file in ["normal_prompt.txt", "sensitive_prompt.txt"]:
        prompts = get_csvs(os.path.join(ori_outputs, txt_file))

        TargetLanguage = target_language
        f = open(f"{ori_outputs}/{TargetLanguage}_{txt_file}", "w")
        for i in tqdm(prompts):
            i = i.strip()
            if len(i) > 5000:
                continue
            # print(i)
            body = {
                'TargetLanguage': TargetLanguage,
                'TextList': [i],
            }
            try:
                res = service.json('translate', {}, json.dumps(body))
                print(res)
                returns = json.loads(res)["TranslationList"][0]["Translation"]
                returns = str(returns).encode("utf-8").decode("utf-8")
                # print(returns)
                txts = returns.strip() + "\n"
                print(txts)
                f.write(txts)
            except Exception as ex:
                print(ex)
        f.close()

