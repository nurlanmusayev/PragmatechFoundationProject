let ededler=[1,3,4,90,23,890,12,30,4,3,67,21];

//Task 01//
let cem=0;
function cemEdedler(massiv){
    for(i=0;i<massiv.length;i++){
        cem+=massiv[i];
    }
    return cem;

}

console.log(cemEdedler(ededler))

//Task 02//
let cemCut=0;
function cemCutler(massiv){
    for(i=0;i<massiv.length;i++){
        if(massiv[i]%2==0)
        cemCut+=massiv[i];
    }
    return cemCut;
}

console.log(cemCutler(ededler))

//Task 03//
let cemTek=0;
function cemTekler(massiv){
    for(i=0;i<massiv.length;i++){
        if(massiv[i]%2)
        cemTek+=massiv[i];
    }
    return cemTek;
}

console.log(cemTekler(ededler))






       
     