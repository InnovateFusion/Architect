import { AppBar, Dialog } from '@mui/material';
import React, { Component, useCallback } from 'react';
import LoadingScreen from '../components/loading-screen/LoadingScreen';
import Question from '../sections/demo/question';
import axios from '../utils/axios';
import ResultForm from '../sections/demo/form';
// import FormUserDetails from './FormUserDetails';
// import FormPersonalDetails from './FormPersonalDetails';
// import Confirm from './Confirm';
// import Success from './Success';

export class UserForm extends Component {
  state = {
    step: 0,
    title: 'Electical Engineering',
    type: 'home',
    question1: 'A. Office Space',
    question2: 'C. 50,000 - 100,000 sq ft',
    question3: 'A. Modern',
    question4: 'B. Energy Efficiency',
    question5: 'C. 4-6 Floors',
    question6: "D. Local authorities' approval required",
    question7: 'B. 50-200',
    question8: 'C. Mix of specialized and standard spaces',
    question9: 'B. Basic accessibility features',
    question10: 'B. Basic amenities',
    question11: 'C. Sufficient parking for employees and visitors',
    question12: 'C. Contemporary and Open',
    question13: 'A. Brand Colors and Logo',
    question14: 'D. All of the above',
    interest: 'none',
    start: '',
  };

  questions = [
    {
      question_number: 0,
      key: 'start',
      question:
        "Hello, I'm the Architect. \n I will ask you a couple of personalized questions to understand your preference and help you Design your dream Home.",
      options: [
        'A. Aging in place',
        'B. Accommodating a home office',
        'C. Energy Efficiency',
        'D. Sustainable Design',
      ],
    },
    {
      question_number: 1,
      key: 'question1',
      question:
        "Are there specific future-proofing considerations you'd like to address in the design to accommodate changing needs over time?",
      options: [
        'A. Aging in place',
        'B. Accommodating a home office',
        'C. Energy Efficiency',
        'D. Sustainable Design',
      ],
    },
    {
      question_number: 2,
      key: 'question2',
      question:
        'Are there any cultural or religious considerations that should be integrated into the design?',
      options: [
        'A. Prayer Room',
        'B. Cultural Symbolism',
        'C. Meditation Space',
        'D. Traditional Artifacts',
      ],
    },
    {
      question_number: 3,
      key: 'question3',
      question: 'What is the budget range you are considering for your residential project?',
      options: [
        'A. $10,000 - $50,000',
        'B. $50,000 - $100,000',
        'C. $100,000 - $250,000',
        'D. Over $250,000',
      ],
    },
    {
      question_number: 4,
      key: 'question4',
      question: 'How many family members will be residing in the home?',
      options: ['A. 0', 'B. 1-3', 'C. 4 - 7', 'D. 8+'],
    },
    {
      question_number: 5,
      key: 'question5',
      question: 'Do you have any specific security or safety requirements for your home?',
      options: ['A. Security System', 'B. Childproofing', 'C. Both', 'D. None'],
    },
    {
      question_number: 6,
      key: 'question6',
      question:
        'Do you require any outdoor spaces like a garden, patio, or playground for children?',
      options: ['A. Garden', 'B. Patio', 'C. Playground', 'D. None'],
    },
    {
      question_number: 7,
      key: 'question7',
      question:
        'How many vehicles do you own, and do you need a garage or parking spaces for them?',
      options: ['A. No', 'B. 1', 'C. 2', 'D. 3'],
    },
    {
      question_number: 8,
      key: 'question8',
      question:
        'How would you prioritize budget allocation across different aspects of the project?',
      options: ['A. Construction', 'B. Interior Finish', 'C. Landscaping', 'D. Equal allocation'],
    },
    {
      question_number: 9,
      key: 'question9',
      question: 'What is the desired size of your home space in square meters?',
      options: [
        'A. 100 square meters',
        'B. 300+ square meters',
        'C. 500+ square meters',
        'D. 1000+ square meters',
      ],
    },
    {
      question_number: 10,
      key: 'question10',
      question:
        'How would you describe your desired atmosphere or ambiance for the interior and exterior spaces?',
      options: ['A. Cozy', 'B. Minimalist', 'C. Elegant', 'D. Modern'],
    },
    {
      question_number: 11,
      key: 'question11',
      question:
        "Are there any specific design inspirations, such as a favorite vacation destination or art movement, that you'd like to draw upon for interior design?",
      options: ['A. Color Picker', 'B. Vintage', 'C. Contemporary', 'D. Natural'],
    },
    {
      question_number: 12,
      key: 'question12',
      question:
        'Are you open to incorporating smart home technology for automation and control of various home systems?',
      options: ['A. Security', 'B. Lighting', 'C. Entertainment', 'D. All of the above'],
    },
    {
      question_number: 13,
      key: 'question13',
      question:
        'Are there any weather-related concerns or considerations for your project, such as extreme temperatures or heavy rainfall during certain seasons?',
      options: ['A. Extreme Temperature', 'B. Heavy Raining', 'C. Both', 'D. None'],
    },
    {
      question_number: 14,
      key: 'question14',
      question:
        'Have you thought about construction phasing if you need to occupy parts of the home before the entire project is completed?',
      options: ['A. YES', 'B. NO', 'C. Not sure', 'D. Partial occupancy planned'],
    },
    {
      question_number: 15,
      key: 'interest',
      question: 'Please add any additional thing to you want to be considered for the design.',
      options: ['A. YES', 'B. NO', 'C. Not sure', 'D. Partial occupancy planned'],
    },
  ];

  // Proceed to next step
  nextStep = () => {
    const { step } = this.state;
    this.setState({
      step: step + 1,
    });
  };

  // Go back to prev step
  prevStep = () => {
    const { step } = this.state;
    this.setState({
      step: step - 1,
    });
  };

  // Handle fields change
  handleChange = (key, option) => {
    if (typeof this.state[key] === 'string') {
      this.setState({ [key]: option });
    } else this.state[key].push(option);
    if (key !== 'interest') this.nextStep();
  };

  business = {
    title: 'Electical Engineering',
    type: 'business',
    question1: 'A. Office Space',
    question2: 'C. 50,000 - 100,000 sq ft',
    question3: 'A. Modern',
    question4: 'B. Energy Efficiency',
    question5: 'C. 4-6 Floors',
    question6: "D. Local authorities' approval required",
    question7: 'B. 50-200',
    question8: 'C. Mix of specialized and standard spaces',
    question9: 'B. Basic accessibility features',
    question10: 'B. Basic amenities',
    question11: 'C. Sufficient parking for employees and visitors',
    question12: 'C. Contemporary and Open',
    question13: 'A. Brand Colors and Logo',
    question14: 'D. All of the above',
    question15: 'D. All of the above',
  };
  data = {};

  analyze = async () => {
    const { step } = this.state;
    this.setState({
      step: -1,
    });
    console.log(this.state);
    const response = await axios.post(
      'https://architect-n16u.onrender.com/api/v1/users/d00bfa01-0697-401a-88db-b6a6d9320dbf/homes/residential',
      { ...this.state }
    );
    console.log(response);
    this.data = JSON.parse(response.data.data);
    console.log(this.data)
    this.setState({
      step: -2,
    });
  };

  render() {
    const { step } = this.state;
    if (step == -1) return <LoadingScreen />;
    else if (step == -2) return <ResultForm response={this.data} />;

    return (
      <Dialog open fullWidth maxWidth="md">
        <Question
          analyze={this.analyze}
          keyss={this.questions[step].key}
          question={this.questions[step].question}
          options={this.questions[step].options}
          nextStep={this.nextStep}
          handleChange={this.handleChange}
        />
      </Dialog>
    );
  }
}

export default UserForm;
