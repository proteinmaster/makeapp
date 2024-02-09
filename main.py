import streamlit as st

import pandas as pd

st.title('ムキムキワッショーイ！！')

st.write('pd.DataFrame')

df = pd.DataFrame({
     'ミドルグリップ懸垂': [10,10,10],
     '腕立て伏せ': [25,20,20],
     'ダンベルデッドリフト': [10,10,10],
     'ダンベルスクワット': [10,10,10],
})

#writeはインタラクティブな表のみ表示
st.write(df)    
#dataframeは表の見た目を調整できる
st.dataframe(df.style.highlight_max(axis=0))
#tableは静的で調整可能な表を表示
st.table(df.style.highlight_max(axis=0))

#markdown記述
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""