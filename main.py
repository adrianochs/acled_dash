import yaml


def api_access_tokens():
    """
    Load api access key and username from auth.yaml.
    To obtain auth.yaml, contact Adrian Ochs.

    :return:
    - api_key (str): the api access key
    - api_user (str): user name for api
    """
    ACLED_CONFIG_FILE = 'auth.yaml'

    with open(ACLED_CONFIG_FILE, 'r') as config_file:
        config = yaml.full_load(config_file)

    api_key_ = config['acled']['api_key']
    api_user_ = config['acled']['api_user']

    return api_key_, api_user_


if __name__ == '__main__':
    api_key, api_user = api_access_tokens()
    print(api_key)
    print(api_user)
