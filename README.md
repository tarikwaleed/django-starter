
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
