import jwt 
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
JWT_SECRET =os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def create_token(user_id : int ,days = 7 ) -> str :
  """
  Function that issues a JWT token for a user

  Args:
    user_id (str): The id of the user
    days (int, optional): The number of days the token will be valid. Defaults to 7

  Returns:
    str: The JWT token as string
  """
  payload = {
        'user_id': user_id,
        'iat': datetime.now().timestamp(),
        'exp':( datetime.now() + timedelta(days=days)).timestamp(),
    }
  token = jwt.encode(payload, JWT_SECRET, algorithm= ALGORITHM)
  return token

def decode_token(token : str) -> str:
    """
    Function that decodes a JWT token
    
    Args:
        token (str): The JWT token to decode
    
    Returns:
        str: The decoded token
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    except Exception as e:
        return str(e)
 