class Complex{
    double real, imag;

public:
    Complex(double r=0, double i=0):real(r), imag(i){};
    // 重载为全局函数，要访问私有成员，所以声明为友元
    friend ostream &operator<<(ostream &os, const Complex &c);
    friend istream &operator>>(istream &is, Complex &c);
};

ostream &operator<<(ostream &os, const Complex &c){
    os << c.real << "+" << c.imag << "i";
    return os;
}

istream &operator>>(istream &is, Complex &c){
    string s;
    is >> s;       // 将 a+bi 作为字符串读入
    int pos = s.find("+", 0);
    string s_tmp = s.substr(0, pos);    // 分离出代表实部的字符串
    c.real = atof(s_tmp.c_str());       // atof能将const char *指针指向的内容传唤成float
    s_tmp = s.substr(pos+1, s.length() - pos - 2);
    c.imag = atof(s_tmp.c_str());
    return is;
}