// 1
/*

    itemName 와  itemPrice 는 한쌍이며 , 아이템 이름과 가격을 뜻한다. 

    order 는 오늘 주문받은 리스트이다. 
    1,2,3,0,1,0 은 인덱스 번호이고 , 차례대로 
    감 , 귤 , 수박 , 사과 , 감 , 사과 이렇게 주문받은것이다. 

    cancle 은 주문취소 리스트이다. 
    순서대로 사과 , 수박 , 귤이 취소되었다. 

    오늘의 매출 총액을 구하시오.
*/

itemName = ['사과', '감', '귤', '수박'];
itemPrice = [1000, 1200, 1300, 1400];
order = [1, 2, 3, 0, 1, 0];
cancel = [0, 3, 2];

total = 0;

for (var i = 0; i < order.length; i++) {
  total += itemPrice[order[i]];
  //   console.log(total);
}
for (var i = 0; i < cancel.length; i++) {
  total -= itemPrice[cancel[i]];
  //   console.log(total);
}
console.log(total);

// 2
/*
    [배열]
        랜덤으로 1~9사이의 숫자를 저장한다. 
        arr 배열안에 랜덤숫자있으면 인덱스를 출력
        arr 배열안에 랜덤숫자가 없으면 "x" 를 출력 
    [예시]
        r = 3 : "x"
        r = 7 : 3
*/
arr = [4, 5, 6, 7, 8];
r = parseInt(Math.random() * 9) + 1;
// console.log(r);

chk = false;
idx = 0;
for (var i = 0; i < arr.length; i++) {
  if (arr[i] === r) {
    chk = true;
    idx = i;
  }
}
res = chk ? `r = ${r} : ${idx}` : `r = ${r} : x`;
console.log(res);

// 3
/*
    [문제]
        랜덤숫자 0~4를 8번 반복해서 출력한다. 

        랜덤숫자가 순서대로 1,2,3,2,1,1,2,1
        이와 같이 출력되었다면 , 해당 인덱스의 자리를 1씩 증가한다. 
        단 , arr1배열은 최대 2개만 저장가능하며, 
        추가적으로 같은숫자가 계속 나올경우는 arr2에 저장한다. arr2는 무한으로 저장가능하다. 
    [예시]
        1 : arr1 = [0,1,0,0,0] , arr2 = [0,0,0,0,0]
        2 : arr1 = [0,1,1,0,0] , arr2 = [0,0,0,0,0]
        3 : arr1 = [0,1,1,1,0] , arr2 = [0,0,0,0,0]
        2 : arr1 = [0,1,2,1,0] , arr2 = [0,0,0,0,0]
        1 : arr1 = [0,2,2,1,0] , arr2 = [0,0,0,0,0]
        1 : arr1 = [0,2,2,1,0] , arr2 = [0,1,0,0,0]
        2 : arr1 = [0,2,2,1,0] , arr2 = [0,1,1,0,0]
        1 : arr1 = [0,2,2,1,0] , arr2 = [0,2,1,0,0]
*/
arr1 = [];
arr2 = [];

for (var i = 0; i < 5; i++) {
  arr1.push(0);
  arr2.push(0);
}

randomArr = [];

for (var i = 0; i < 8; i++) {
  r = parseInt(Math.random() * 5);
  randomArr.push(r);
}
// randomArr = [1, 2, 3, 2, 1, 1, 2, 1];
// prev = randomArr[0];
// arr1[randomArr[0]] += 1;

for (var i = 0; i < randomArr.length; i++) {
  if (arr1[randomArr[i]] >= 2) {
    arr2[randomArr[i]] += 1;
  } else {
    arr1[randomArr[i]] += 1;
  }
}

console.log(randomArr);
console.log(arr1);
console.log(arr2);
