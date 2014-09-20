source activate

mkdir bloomberg
cd bloomberg

wget http://static.bloomberglabs.com/api/cpp/blpapi_cpp_3.7.9.1-linux.tar.gz
wget http://static.bloomberglabs.com/api/python/blpapi_python_3.5.5.tar.gz

tar -xvf blpapi_cpp_3.7.9.1-linux.tar.gz
tar -xvf blpapi_python_3.5.5.tar.gz

export BLPAPI_ROOT=$(pwd)/blpapi_cpp_3.7.9.1

cd blpapi-3.5.5
python setup.py install
