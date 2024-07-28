from dotenv import find_dotenv, load_dotenv


#%% Functions
def load_envvar():
    local_env_path = 'setup/.env.local'
    load_dotenv(find_dotenv(local_env_path, raise_error_if_not_found=True))
