echo "Remove    excess      spaces." | tr -s "\b" " "
echo "remove all the as" | tr -d "a"
echo "set to uppercase" | tr [:lower:] [:upper:]
echo "10.00 only numbers 1.33" | tr -d [:alpha:] | tr -s " " ","


