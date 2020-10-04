import os
import tempfile
import shutil
import zipfile
import glob
import base64

data_dir = "..\\data"
base_dir = os.getcwd()


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def get_dirs(path):
    return [os.path.basename(x) for x in filter(
        os.path.isdir, glob.glob(os.path.join(data_dir, path, '*')))]


def get_apis():
    return get_dirs('api')


def get_clients():
    return get_dirs('client')


def get_servers():
    return get_dirs('server')


def get_platforms():
    return get_dirs('platform')


def get_project(api='ASP.NET Core 3.1 EF Core 3.8.1', client='Angular 10', server='Nginx', platform="Docker"):
    path = os.path.dirname(os.path.realpath(__file__))

    output_dir = "."
    tmp_dir = tempfile.mkdtemp()

    api_path = os.path.join(path, f'{data_dir}\\api\\{api}\\*')
    client_path = os.path.join(path, f'{data_dir}\\client\\{client}\\*')
    server_path = os.path.join(path, f'{data_dir}\\server\\{server}\\*')
    platform_path = os.path.join(path, f'{data_dir}\\platform\\{platform}\\*')

    api_path = os.path.dirname(api_path)
    client_path = os.path.dirname(client_path)
    server_path = os.path.dirname(server_path)
    platform_path = os.path.dirname(platform_path)

    shutil.copytree(api_path, f"{tmp_dir}/api/")
    shutil.copytree(client_path, f"{tmp_dir}/client/")
    shutil.copytree(server_path, f"{tmp_dir}/server/")
    shutil.copytree(platform_path, f"{tmp_dir}/", dirs_exist_ok=True)
    # os.chdir(tmp_dir)
    shutil.make_archive('project', 'zip', tmp_dir, '.')

    with open(os.path.join('.', "project.zip"), 'rb') as f:
        message_bytes = f.read()
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message


if __name__ == '__main__':
    apis = get_apis()
    print(apis)
    # x = get_project()
    # print(x)
