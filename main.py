import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=500, height=1000)

"""
# 大見出し
## 中見出し
### 小見出し

```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=500, height=1000)
```

"""

st.table(df.style.highlight_min(axis=0))

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [34.55, 135.74],
    columns=['lat', 'lon']
)

st.map(df3)

st.write('Display Image')
img = Image.open('FIREFINE.png')
st.image(img, caption='FIREFINE', use_column_width=True)