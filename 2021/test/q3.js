const numOfFreinds = 2;
// const freindsList = [
//   {
//     position: 10,
//     speed: 4,
//     r: 3,
//   },
//   {
//     position: 20,
//     speed: 4,
//     r: 2,
//   },
// ];
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

const centerPoint = (freindsList) => {
  let sum = 0;
  for (let i = 0; i < freindsList.length; i++) {
    sum += freindsList[i].position;
  }
  return Math.round(sum / numOfFreinds);
};

const weightCenterPoint = (friendsList) => {
  let weightedSum = 0;
  let totalWeight = 0;

  for (let i = 0; i < friendsList.length; i++) {
    const { position, speed } = friendsList[i];
    weightedSum += position * speed;
    totalWeight += speed;
  }

  // Calculate the weighted average and round to the nearest integer
  return Math.round(weightedSum / totalWeight);
};

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

const weightCalcTrueCenter = (friendsList) => {
  const center = weightCenterPoint(friendsList);
  let weightedDistanceSum = 0;
  let totalWeight = 0;

  for (let i = 0; i < friendsList.length; i++) {
    const { position, speed, r } = friendsList[i];
    const distance = Math.abs(position - center);

    // Determine if the center is within the range of the current friend
    if (
      (position < center && position + r > center) ||
      (position > center && position - r < center)
    ) {
      weightedDistanceSum += distance * speed;
    } else if (position < center) {
      weightedDistanceSum += (center - (position + r)) * speed;
    } else if (position > center) {
      weightedDistanceSum += (position - r - center) * speed;
    }

    totalWeight += speed;
  }

  // Calculate the weighted average distance and round to the nearest integer
  return Math.round(weightedDistanceSum / totalWeight);
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

console.log(calcRemainingTime(freindsList, calcTrueCenter(freindsList) + 2));

// console.log(centerPoint(freindsList), weightCenterPoint(freindsList));
