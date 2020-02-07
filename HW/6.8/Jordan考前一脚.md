#若当标准型Jordan Normal/Canonical Form的一些理解



一、基础概念

1. Nilpotent 幂零
   $$
   \\N = 
   	\left[
   	\begin{matrix}
   	0 & 1 & 0 & \ldots & 0 \\
     0         & 0 & 1 & \ldots & 0 \\
     \vdots    & \vdots & \vdots   & \ddots & \vdots \\
     0         & 0     & 0  & \ldots &  1 \\
     0         & 0     & 0  & \ldots &  0 \\
   	\end{matrix}
   	\right]
   $$
   

2. 矩阵Jordan block若当块
   $$
   \\J_{\lambda_i} = 
   	\left[
   	\begin{matrix}
   	\lambda_i & 1 & \ldots & 0 \\
     0         & \lambda_i & \ldots & 0 \\
     \vdots    & \vdots   & \ddots & \vdots \\
     0         & 0       & \ldots &  \lambda_i \\
   	\end{matrix}
   	\right]
   	=\lambda_i I+N
   $$

3. Jordan Normal Form 若当标准型

   定理描述：任何矩阵在complex field上必定与一Upper Triangular矩阵相似，进一步，这个上三角阵具有以下形状
   $$
   A \sim J 或  A = BJB^{-1}，B=(v_1, v_2, ..., v_n)，其中v_i是空间V下的一组基\\
   J = diag(J_1, J_2, \dots, J_a),其中J_i均为Jordan Block，且特征值均为A的特征值
   $$
   注意：一个特征值可能对应多个Jordan Block。

   问题是，怎么确定每一个特征值所对应的Jordan Block的数量以及各自的大小？我们需要反过来利用幂零Nilpotent的性质，并且定义广义特征向量（generalized eigenvectors）以及其不变子空间

4. 幂零的性质

   1. 如果给定一个线性变换（或者它在V的一组基下矩阵N）是nilpotent的，这说的是，存在一个正整数n为其幂零指数（nilpotent exponent）, s.t $$N^n=O$$。

   2. 根据定义，Jordan Block $$J_{\lambda_i} - \lambda_i I = N$$是幂零的

   3. 回忆，如果A与一个Jordan Block相似，那么有
      $$
      A =  BJ_{\lambda_i}B^{-1}\\
      J_{\lambda_i} - \lambda_i I = N \\
      B(J_{\lambda_i} - \lambda_i I)B^{-1} = BJ_{\lambda_i} B^{-1} - \lambda_i BIB^{-1}=A-\lambda_i I \\
      (BNB{-1})^n=BNB^{-1}BNB^{-1}\dots BNB^{-1} = BN^{n}B^{-1}=O
      $$
      因此，$$A-\lambda_i I$$幂零。

      回忆，我们在对实对称阵进行对角化的时候，利用所有（for all）特征值的代数重数（Algebric Counting Multiplicity，特征多项式中$$x-\lambda_i$$项的指数）和几何重数（Geometirc Counting Multiplicity，特征子空间的维数，也就是特征向量eigenvector的总数）相等的条件。

      进行求解时我们通过求解$$(A-\lambda_iI)\vec x=O$$方程，这个方程的解都满足$$A\vec x = \lambda_iI \vec x$$，因而他们都是关于$$\lambda_i$$的eigenvector，解空间就是属于特征值$$\lambda_i$$的特征子空间。我们知道，解空间可以看作某一个线性变换/矩阵的kernel，所以接下来我们都用"代数的语言"、称解空间为$$(A-\lambda_iI)$$的kernel。

   解下来我们来看一般的情况，也就是代数重数！=几何重数（事实上几何重数一定小于代数重数，于是这里产生了空缺，这些空缺如果被填上了，那么就和之前的"理想条件“类似，实现了对角化）。因而我们引入"广义特征向量（空间）"来填补这里的空缺。

5. 广义特征向量（generalized eigenvectors）及其空间

   我们刚才讨论过，$$A-\lambda_iI$$是超好型：如果$$\lambda_i$$的ACM=GCM，则解方程得到$$\lambda_i$$的所有特征向量；现在ACM！=GCM，我们仍然有，$$A-\lambda_iI$$是幂零的。

   那么，根据"特征空间与解空间"的关系，我们迁移概念，把各个幂次的$$A-\lambda_iI$$的kernel称为广义特征空间，那么其中的元素就是广义特征向量。

6. 所以Jordan标准型怎么求？

   其实我不想给标准化的解法（记忆麻烦），给一个直观的操作，依葫芦画瓢就可以求。

   刚才讨论过kernel。进一步查看幂零阵的kernel。记N=$$A-\lambda_iI$$，幂零指t：

   $$N^{t}=O$$ ，因而$$N^{t}=O$$的kernel就是V自身

   $$Nx=O$$，我们知道其kernel就是$$\lambda_i$$的所有特征向量，i.e. 特征子空间$$V_{\lambda_i}$$。

   给出以下Lemma1：
   $$ {Lemma1}
   Lemma 1: I = ker (A-\lambda_i I)^0 \le ker(A-\lambda_i I) \le ker(A-\lambda_i I)^2 \le \dots \le ker(A-\lambda_i I)^t = V
   $$
   其中的小于号表示"包含于"。

   该lemma的证明显然，即任取前一个空间中元素v，用$$(A-\lambda_i I)$$更高的幂次apply to it，肯定是0，也就是kernel的定义。

   那么，由Lemma，
   $$
   Cor1: n = dimV = dimKer (A-\lambda_i I)^{t} \ge dim Ker(A-\lambda_i I)^{t-1} \ge \dots \ge dimKer(A-\lambda_i I) \ge dimKer(A-\lambda_i I)^0 = dimKerI = 0
   $$
   事实上，所有的大于等于号都是大于，【并且前一项比后一项至少大1】（因而如果把它们看成一个函数图像的话，有点像单位圆在第一象限中的曲线，没错指它的"凸性"）

   我们的任务是找出这个kernel序列中两个相邻空间之间的"差"（注意与商空间quotient space的区别），有了这些差我们就可以"填补"之前说的空白了。接下来我们先来看Jordan标准型的一个求法：

   我们任取$$ker(A-\lambda_i I)^{t}$$中的元素$$v_1$$。我们发现

   $$v_1 \in ker(a - \lambda_i I)^{t},\\   ( A-\lambda_i I)v_1 \in ker(A-\lambda_i I)^{t-1}, \\ (A-\lambda_i I)^{2}v_1 \in ker(A-\lambda_i I)^{t-2}, \\ \dots\\ (A-\lambda_i I)^{t-1}v_1 \in ker(A-\lambda_i I)^{1}$$

   并且，我们意识到他们都是线性无关的（使用定义证明，在等式的左方apply $$A-\lambda_i I$$ ），那么我们找到了一组基，这组基是幂零的这组基下A的矩阵是一个幂零矩阵。

   这样子的描述可能不够清楚，下面是一个例子，这个例子给出了Jordan标准型的求法

![avatar](/Users/chenwei/Desktop/linkao/fig1.png)

![avatar](/Users/chenwei/Desktop/linkao/fig2.png)

​	因而，我们可以总结Jordan标准型的一种求法：

​		a. 求出A的所有特征值与ACM

​		b. 对于某个特征值，计算$$A-\lambda_iI$$ 的解空间，即GCM

​			如果GCM=ACM，那么这个特征值有ACM个若当块，每个块都是$$1\times1$$大小；

​			如果GCM<ACM，那么我们需要借助广义特征向量：

​				先计算幂零阵$$A-\lambda_iI$$的幂零指数t，这个过程中的副产品就是各阶$$A-\lambda_iI$$，把它们记录在草稿纸上，并且观察它们的rank，由rank推算其kernel的dim

​				现在，我们把各个kernel摆成例子中的样子（这样子比较直观）

​				按照例子中的方法，从V中任取一个向量$$v_i$$（这个向量可以自己选得越简单越好），由于我们的各个引理条件，就得到$$v_i, (A-\lambda_iI)v_1, \dots, (A-\lambda_iI)^{t-1}v_i$$这样的一组基。从底下（次数大的）往上看，由于它的"凸性"，如果dim(下面)-dim(上面) > 1，那么它们的“gap”就不仅仅是$$v_i$$基序列造成的，我们找到"罪魁祸首"$$v_2$$，并且也类似地生成一个基序列。如此程序化操作，我们就得到了"一串串"的基序列。每个基序列都对应一块Jordan block。这样子我们就找到了了$$\lambda_i$$的所有Jordan block和相应的基（可以拼凑成B）

​		c. 对于所有的$$lambda$$，重复执行b，按照例子中（第二张图片第一行）的顺序排列基，得到了标准型

这里描述的这个算法，与鲁自群老师给的总结中的解法是一致的，不过从这个角度来看个人感觉失误率降低很多。



二、一些补充

 1. 为什么要Jordan标准型？

    其实我们从代数的角度来看，一个线性变换的性质只和它自己有关系，矩阵和线性空间的同构关系表明一切矩阵都可以看作是一个线性算子。

    那什么是矩阵？事实上，矩阵就是某一个线性算子在给定的基下的坐标表示，如果我们有不同的基，就有不同的矩阵（但它们是相似的）。

    因而，我们Jordan标准型分解和对角化的出发点是一致的：找到一组"漂亮的基"，这组基下面，这个线性变换/矩阵的表示方法非常"干净整洁"。

2. 期末考中Jordan标准型应该仍然是重头戏……