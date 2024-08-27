"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "AWS_KMS" + os.sep + "libs" + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)
    
import os
import sys
from kmsObject import kmsObject
global session_kms_connect
module = GetParams("module")

try:
    if module == "connect":
        awsAccessKeyId = GetParams("access_id")
        awsSecretAccessKey = GetParams("secret_key")
        regionName = GetParams("regionName")
        var_ = GetParams('var_')

        try:
            session_kms_connect = kmsObject(awsAccessKeyId, awsSecretAccessKey, regionName)
            connect = True
        except ValueError:
            connect = False
        SetVar(var_, connect)

    if module == "createKey":
        var_ = GetParams('var_')
        description_ = GetParams('description_')
        try:
            key_metadata = session_kms_connect.create_key(description=description_)
            if key_metadata:
                key_id = key_metadata['KeyId']
                SetVar(var_, key_id)
        except Exception as e:
            import traceback
            traceback.print_exc()
            SetVar(var_, connect)

    if module == "encrypt":
        key_id= GetParams("key_id")
        text = GetParams("text")
        var_ = GetParams('var_')

        try:
            res = session_kms_connect.encrypt(key_id, text)
            SetVar(var_, res)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

    if module == "decrypt":
        ciphertext_blob = GetParams("ciphertext_blob")
        var_ = GetParams('var_')
        try:
            res = session_kms_connect.decrypt(ciphertext_blob)
            SetVar(var_, res)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e
    
    if module == "list_key":
        var_ = GetParams('var_')
        try:
            res= []
            keys = session_kms_connect.list_keys()
            if keys:
                res.append("List of Key IDs:")
                for key in keys:
                    print(key['KeyId'])
            
            SetVar(var_, keys)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e