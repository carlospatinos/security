MODE=$1
MESSAGE=$2

for i in {1..26}; do  
    OUT=$(python caesarCypher.py $MODE $i "$MESSAGE")
    echo "$i -> $OUT";
done

