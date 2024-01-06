## To run the project
**steps without details**

- [ ] instll docker
- [ ] create ssh key pair
- [ ] add the public ssh key to bitbucket
- [ ] clone the project
- [ ] copy `.env` file
- [ ] run the containers
- [ ] exec into the api container and migrate
____________________________
## How to log exceptions

```python
import traceback
from datetime import datetime
with open("/applogs/exceptions.log", "a") as file:
    file.write(
        f"an error happened at {datetime.datetime.now()}\n"
    )
    file.write(f"Exception details: {str(e)}\n")
    file.write(f"Full traceback: \n{traceback.format_exc()}\n")
    file.write("-------------------------------------------------------")
```
