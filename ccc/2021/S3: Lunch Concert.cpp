#include <iostream>
#include <vector>
using namespace std;
#define ll long long

class Person
{
public:
    ll position;
    ll speed;
    ll r;

    Person() : position(0), speed(0), r(0) {}

    Person(ll position, ll speed, ll r) : position(position), speed(speed), r(r) {}
};

int weightCenterPoint(const vector<Person> &list)
{
    ll weightedSum = 0;
    ll totalWeight = 0;

    for (const auto &person : list)
    {
        weightedSum += person.position * person.speed;
        totalWeight += person.speed;
    }

    return weightedSum / totalWeight;
}

int calcTrueCenter(const vector<Person> &list)
{
    ll center = weightCenterPoint(list);
    ll distance = 0;

    for (const auto &person : list)
    {
        if (
            (person.position < center &&
             person.position + person.r > center) ||
            (person.position > center &&
             person.position - person.r < center))
        {
            distance += center;
        }
        else if (person.position < center)
        {
            distance += person.position + person.r;
        }
        else if (person.position > center)
        {
            distance += person.position - person.r;
        }
    }
    return distance / list.size();
}

ll calcRemainingTime(const vector<Person> &friendsList, ll center)
{
    ll time = 0;
    for (const auto &person : friendsList)
    {
        ll distanceLeft = 0;

        if (
            (person.position < center &&
             person.position + person.r > center) ||
            (person.position > center &&
             person.position - person.r < center))
        {
            time += 0;
        }
        else if (person.position < center)
        {
            distanceLeft = center - (person.position + person.r);
            time += distanceLeft * person.speed;
        }
        else if (person.position > center)
        {
            distanceLeft = person.position - center - person.r;
            time += distanceLeft * person.speed;
        }
    }
    return time;
}

ll gradientDescent(const vector<Person> &friendsList, ll base, ll center)
{
    ll currentCenter = center;

    ll minsTen = calcRemainingTime(friendsList, currentCenter - 10);
    ll plusTen = calcRemainingTime(friendsList, currentCenter + 10);

    if (minsTen < base)
    {
        return gradientDescent(friendsList, minsTen, currentCenter - 10);
    }
    if (plusTen < base)
    {
        return gradientDescent(friendsList, plusTen, currentCenter + 10);
    }

    ll minsFive = calcRemainingTime(friendsList, currentCenter - 10);
    ll plusFive = calcRemainingTime(friendsList, currentCenter + 10);

    if (minsFive < base)
    {
        return gradientDescent(friendsList, minsFive, currentCenter - 5);
    }
    if (plusFive < base)
    {
        return gradientDescent(friendsList, plusFive, currentCenter + 5);
    }

    ll minsTwo = calcRemainingTime(friendsList, currentCenter - 2);
    ll plusTwo = calcRemainingTime(friendsList, currentCenter + 2);

    if (minsTwo < base)
    {
        return gradientDescent(friendsList, minsTwo, currentCenter - 2);
    }
    if (plusTwo < base)
    {
        return gradientDescent(friendsList, plusTwo, currentCenter + 2);
    }

    ll minsOne = calcRemainingTime(friendsList, currentCenter - 1);
    ll plusOne = calcRemainingTime(friendsList, currentCenter + 1);

    if (minsOne < base)
    {
        return gradientDescent(friendsList, minsOne, currentCenter - 1);
    }
    if (plusOne < base)
    {
        return gradientDescent(friendsList, plusOne, currentCenter + 1);
    }
    return base;
}

int main()
{
    int numOfPeople;
    cin >> numOfPeople;

    vector<Person> people(numOfPeople);

    for (int i = 0; i < numOfPeople; i++)
    {
        ll p, s, r;
        cin >> p >> s >> r;

        people[i] = Person(p, s, r);
    }

    cout << gradientDescent(
        people,
        calcRemainingTime(people, calcTrueCenter(people)),
        calcTrueCenter(people));

    return 0;
}
