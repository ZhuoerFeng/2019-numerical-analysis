function x=gaosixiaoqu(A,b,n)
%将矩阵化成上三角阵
for k=1:(n-1)
    for i=(k+1):n
        piv=A(i,k)/A(k,k);
        b(i)=b(i)-piv*b(k);
        for j=k:n
            A(i,j)=A(i,j)-piv*A(k,j);
        end
    end
end
clear i
clear j
clear k
%高斯消去解方程
x=zeros(n,1);
x(n)=b(n)/A(n,n);
for i=(n-1):-1:1
        for j=(i+1):n
            x(i)=-x(j)*A(i,j)/A(i,i)+x(i);
        end
        x(i)=x(i)+b(i)/A(i,i);
end
