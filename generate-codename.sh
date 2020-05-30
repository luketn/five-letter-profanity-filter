set -e
set +x

#Generate a codename
NAME=$(shuf -n 1 five-letter-words.txt)
NUMBER=$((RANDOM%=99))
export CODENAME="${NAME}${NUMBER}"

# Write the codename to the console
echo "Codename selected: ${CODENAME}"
