# Leet-Code-Submissions
Repository to keep track of my leetcode submissions



# Equation
$max_{\alpha \geq 0} min_{w,b} [\frac{1}{2}||w||^2 - \sum_j\alpha_j[(wx_j + b)y_j] - 1]$


$\frac{\nabla L}{\nabla w} =  w - \sum_j\alpha_jx_jy_j = 0 $ 

$\implies w = \sum_j\alpha_jy_jx_j$

$\frac{\nabla L}{\nabla b} = -\sum_j\alpha_jy_j = 0$ 


b -> Gradient Descent 


$b_{new} = b - \eta*(-\sum_j\alpha_jy_j)$

___

$max_{\alpha \geq 0}  [\frac{1}{2}||\sum_i\alpha_iy_ix_i||^2 - \sum_j\alpha_j[(\sum_i\alpha_iy_ix_ix_j)y_j] - 1]$

$max_{\alpha \geq 0} \sum_j\alpha_j + -\frac{1}{2}\sum_j\alpha_jy_jx_j[\sum_i\alpha_iy_ix_i  ]$ 



$\max_{\alpha \geq 0} \sum_j \alpha_j - \frac{1}{2}\sum_{i,j}y_iy_j\alpha_i\alpha_hx_jx_i$


___

```python3

```