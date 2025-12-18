from cryptography.fernet import Fernet

key = b'G5EmOTK3hCUMYT_xBzwQWbZO3jx-avQN23BgDWzeLrA='

# Use plain text credentials (simplifies testing)
# If you need encryption, encrypt them first with Fernet(key).encrypt(b'value')
user_name = "standard_user"
password = "secret_sauce"