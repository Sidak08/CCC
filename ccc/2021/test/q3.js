const freindsList = [
  {
    position: 6,
    speed: 8,
    r: 3,
  },
  {
    position: 1,
    speed: 4,
    r: 1,
  },
  {
    position: 14,
    speed: 5,
    r: 2,
  },
];
// const freindsList = [
//   {
//     position: 0,
//     speed: 10000,
//     r: 0,
//   },
// ];

const weightCenterPoint = (freindsList) => {
  let weightedSum = 0;
  let totalWeight = 0;

  for (let i = 0; i < freindsList.length; i++) {
    const { position, speed } = freindsList[i];
    weightedSum += position * speed;
    totalWeight += speed;
  }

  // Calculate the weighted average and round to the nearest integer
  return Math.round(weightedSum / totalWeight);
};

// const weightCalcTrueCenter = (freindsList) => {
//   const center = weightCenterPoint(freindsList);
//   let weightedDistanceSum = 0;
//   let totalWeight = 0;

//   for (let i = 0; i < freindsList.length; i++) {
//     const { position, speed, r } = freindsList[i];
//     const distance = Math.abs(position - center);

//     // Determine if the center is within the range of the current friend
//     if (
//       (position < center && position + r > center) ||
//       (position > center && position - r < center)
//     ) {
//       weightedDistanceSum += distance * speed;
//     } else if (position < center) {
//       weightedDistanceSum += (center - (position + r)) * speed;
//     } else if (position > center) {
//       weightedDistanceSum += (position - r - center) * speed;
//     }

//     totalWeight += speed;
//   }

//   // Calculate the weighted average distance and round to the nearest integer
//   return Math.round(weightedDistanceSum / totalWeight);
// };

const calcTrueCenter = (freindsList) => {
  center = weightCenterPoint(freindsList);
  let distance = 0;
  for (let i = 0; i < freindsList.length; i++) {
    if (
      (freindsList[i].position < center &&
        freindsList[i].position + freindsList[i].r > center) ||
      (freindsList[i].position > center &&
        freindsList[i].position - freindsList[i].r < center)
    ) {
      distance += center;
    } else if (freindsList[i].position < center) {
      distance += freindsList[i].position + freindsList[i].r;
    } else if (freindsList[i].position > center) {
      distance += freindsList[i].position - freindsList[i].r;
    }
  }
  return Math.round(distance / freindsList.length);
};

const calcRemainingTime = (freindsList, center) => {
  // missing the hit logic
  let time = 0;
  for (let i = 0; i < freindsList.length; i++) {
    let distanceLeft = 0;

    if (
      (freindsList[i].position < center &&
        freindsList[i].position + freindsList[i].r > center) ||
      (freindsList[i].position > center &&
        freindsList[i].position - freindsList[i].r < center)
    ) {
      time += 0;
    } else if (freindsList[i].position < center) {
      distanceLeft = center - (freindsList[i].position + freindsList[i].r);
      time += distanceLeft * freindsList[i].speed;
    } else if (freindsList[i].position > center) {
      distanceLeft = freindsList[i].position - center - freindsList[i].r;
      time += distanceLeft * freindsList[i].speed;
    }
  }
  return time;
};

const gradeintDecent = (freindsList, base, center) => {
  const currentCenter = center;
  const minsOne = calcRemainingTime(freindsList, currentCenter - 1);
  const plusOne = calcRemainingTime(freindsList, currentCenter + 1);

  console.log(
    `Current base: ${base}, minsOne: ${minsOne}, plusOne: ${plusOne}, center ${currentCenter}`,
  );

  // Recursive descent if conditions are met
  if (minsOne < base) {
    console.log("Going to minsOne", currentCenter - 1);
    return gradeintDecent(freindsList, minsOne, currentCenter - 1);
  }
  if (plusOne < base) {
    console.log("Going to plusOne", currentCenter + 1);
    return gradeintDecent(freindsList, plusOne, currentCenter + 1);
  }

  // Return the best value found
  console.log(`Final base value: ${base}`);
  return base;
};

console.log(
  gradeintDecent(
    freindsList,
    calcRemainingTime(freindsList, calcTrueCenter(freindsList)),
    calcTrueCenter(freindsList),
  ),
);

console.log(weightCenterPoint(freindsList));
console.log(calcTrueCenter(freindsList));
console.log(calcRemainingTime(freindsList, calcTrueCenter(freindsList)))
