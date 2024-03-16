// Czy liczba m jest potega n czyli m = n**k, gdzie m, n >= 2, k nalezy do C

function IsPower(m, n) {
    if (m == 1)
        return (n == 1);
    k = 1;
    while (p < n) {
        k *= m;
    }
    return k == n;
}

function main() {
    console.log(IsPower(10, 1));
    console.log(IsPower(1, 20));
    console.log(IsPower(2, 128));
    console.log(IsPower(2, 30));
    return 0;
    
}

main();