if [[ ${PWD##*/} != "tests" ]] ;
then 
    echo "Failed: please run this script from DeepKS/tests/";
else
    cd ../..

    python3 -m DeepKS.api.main -k TCHKGIDKMMRMQHAMLPLQMYLCF,YVMLYNNGPLWGRNDMMSCKSYVHD,HHMCEFCCAMCPQDGWHLMTAFGHD -s VQQEPGWTCYLFSYV,NHSVNQHWANFTCNR,ALVVNQRDKSYNAQA -p dictionary_json

    python3 -m DeepKS.api.main -k TCHKGIDKMMRMQHAMLPLQMYLCF,YVMLYNNGPLWGRNDMMSCKSYVHD,HHMCEFCCAMCPQDGWHLMTAFGHD -s VQQEPGWTCYLFSYV,NHSVNQHWANFTCNR,ALVVNQRDKSYNAQA -p in_order_json

    python3 -m DeepKS.api.main -k TCHKGIDKMMRMQHAMLPLQMYLCF,YVMLYNNGPLWGRNDMMSCKSYVHD,HHMCEFCCAMCPQDGWHLMTAFGHD -s VQQEPGWTCYLFSYV,NHSVNQHWANFTCNR,ALVVNQRDKSYNAQA -p in_order -v

    python3 -m DeepKS.api.main -k TCHKGIDKMMRMQHAMLPLQMYLCF,YVMLYNNGPLWGRNDMMSCKSYVHD,HHMCEFCCAMCPQDGWHLMTAFGHD -s VQQEPGWTCYLFSYV,NHSVNQHWANFTCNR,ALVVNQRDKSYNAQA -p dictionary -v

fi