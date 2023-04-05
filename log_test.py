import logging
logging.basicConfig(
    filename="test_log.txt", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%y %I:%M:%S %p'
)

logging.info('*************************')
logging.info("*******New request*******")

import traceback
d = {1:12,2:13}
try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print(a//b)
    i = int(input("Enter key : "))
    print(d[i])
except Exception as msg:
    print("Check code .....",msg)
    traceback.print_exc()
    logging.exception(msg)
    logging.info("____Process Failed_____")
else:
    print("Try block executed successfully....")
    logging.info("____Process Successfull_____")
finally:
    print("I'm immortal......")
    
    
print("application executed successfully...")