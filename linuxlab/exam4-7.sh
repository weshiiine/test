#!/bin/bash
# input data
if (( ${#}<1 ))
then
echo "Usage: ${0} num1 num2..."
exit 1
fi
i=0
for k in ${*}
do
data[$i]=${k}
((i++))
done
# sort data
len=${#data[@]}
for (( i=0 ; i<$len-1 ; i++ ))
do
for (( j=i+1 ; j<$len ; j++ ))
do
if [ ${data[$i]} -gt ${data[$j]} ]
then
tmp=${data[$i]}
data[$i]=${data[$j]}
data[$j]=${tmp}
fi
done
done
# display data
for k in ${data[*]}
do
echo -n "${k} "
done
echo
