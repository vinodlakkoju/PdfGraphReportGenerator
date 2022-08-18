from ReportsService.Utils import Utils
from ReportsService.Constants import null


def main():
    ut = Utils()
    data = [
    {
        "self_rec_id": 152,
        "username": "Eva",
        "vacancy_id": null,
        "authoritarian": 60,
        "prospecting": 50,
        "competitive": 55,
        "planning": 38,
        "organising": 0,
        "achieving": 39,
        "pedantic": 50,
        "standardising": 50,
        "critical": 50,
        "influencing": 50,
        "pioneering": 50,
        "dare_devil": 50,
        "strategic": 50,
        "purposeful": 50,
        "encouraging": 50,
        "watchful": 50,
        "preserving": 50,
        "preventative": 50,
        "charismatic": 50,
        "impetuous": 50,
        "hedonistic": 50,
        "visualiser": 61,
        "creative": 100,
        "visionary": 62,
        "harmonising": 45,
        "sympathetic": 50,
        "flattering": 40,
        "assertiveness": 0,
        "confident": 0,
        "persistant": 0,
        "logical": 0,
        "accountable": 0,
        "credibility": 0,
        "attentive": 0,
        "regulating": 0,
        "judgemental": 0,
        "expressive": 0,
        "curious": 0,
        "courageous": 0,
        "effective": 0,
        "insightful": 0,
        "empowering": 0,
        "observant": 0,
        "responsibility": 0,
        "protective": 0,
        "appealing": 0,
        "impulsive": 0,
        "focus": 0,
        "imagination": 0,
        "originality": 0,
        "passion": 0,
        "adaptability": 0,
        "compassionate": 0,
        "gratitude": 0,
        "spontaneous": 50,
        "company_id": null,
        "created_on": "2022-04-13T07:19:15.000Z",
        "updated_on": "2022-04-13T07:19:15.000Z",
        "id": null
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "planning",
        "behaviour_score": 60
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "planning",
        "behaviour_score": 60
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "planning",
        "behaviour_score": 60
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "organising",
        "behaviour_score": 58
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "organising",
        "behaviour_score": 58
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "organising",
        "behaviour_score": 58
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "achieving",
        "behaviour_score": 47
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "achieving",
        "behaviour_score": 47
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "achieving",
        "behaviour_score": 47
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "strategic",
        "behaviour_score": 60
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "strategic",
        "behaviour_score": 60
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "strategic",
        "behaviour_score": 60
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "purposeful",
        "behaviour_score": 72
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "purposeful",
        "behaviour_score": 72
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "purposeful",
        "behaviour_score": 72
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "purposeful",
        "behaviour_score": 72
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Accountable",
        "behaviour_name": "purposeful",
        "behaviour_score": 72
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "purposeful",
        "behaviour_score": 72
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "encouraging",
        "behaviour_score": 40
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "encouraging",
        "behaviour_score": 40
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "encouraging",
        "behaviour_score": 40
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "visualiser",
        "behaviour_score": 53
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "visualiser",
        "behaviour_score": 53
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "visualiser",
        "behaviour_score": 53
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "creative",
        "behaviour_score": 42
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "creative",
        "behaviour_score": 42
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "creative",
        "behaviour_score": 42
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "visionary",
        "behaviour_score": 40
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "visionary",
        "behaviour_score": 40
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Curious",
        "behaviour_name": "visionary",
        "behaviour_score": 40
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "harmonising",
        "behaviour_score": 63
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "harmonising",
        "behaviour_score": 63
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "harmonising",
        "behaviour_score": 63
    },
    {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "sympathetic",
        "behaviour_score": 55
    }, {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "sympathetic",
        "behaviour_score": 55
    }, {
        "company_id": 169,
        "vacancy_id": 27,
        "value_name": "Approachable",
        "behaviour_name": "sympathetic",
        "behaviour_score": 55
    }]
    return_data = ut.constructValuesData(data)
    print(return_data)


if __name__ == '__main__':
    main()
