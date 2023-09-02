import { AppBar, Dialog } from '@mui/material';
import React, { Component } from 'react';
import LoadingScreen from 'src/components/loading-screen/LoadingScreen';
import Question from 'src/sections/demo/question';
// import FormUserDetails from './FormUserDetails';
// import FormPersonalDetails from './FormPersonalDetails';
// import Confirm from './Confirm';
// import Success from './Success';

export class UserForm extends Component {
  state = {
    step: 1,
    title: 'sdds',
    type: 'home',
    future_proofing: [
      'B. Accommodating a home office',
      'C. Energy Efficiency',
      'D. Sustainable Design',
    ],
    cultural_religious: ['B. Cultural Symbolism', 'D. Traditional Artifacts'],
    budget_range: 'C. $100,000 - $250,000',
    family_size: 'B. 1-3',
    security_safety: 'A. Security System',
    outdoor_spaces: 'C. Playground',
    vehicles_parking: 'D. 3',
    budget_allocation: 'B. Interior Finish',
    home_space: 'C. 500+ square meters',
    atmosphere_ambiance: 'A. Cozy',
    design_inspirations: 'B. Vintage',
    smart_home_technology: 'A. Security',
    weather_concerns: 'C. Both',
    construction_phasing: 'C. Not sure',
    interest: '',
  };

  questions = [
    {
      question_number: 1,
      key: 'future_proofing',
      question:
        "Are there specific future-proofing considerations you'd like to address in the design to accommodate changing needs over time? (Select all that apply)",
      options: [
        'A. Aging in place',
        'B. Accommodating a home office',
        'C. Energy Efficiency',
        'D. Sustainable Design',
      ],
    },
    {
      question_number: 2,
      key: 'cultural_religious',
      question:
        'Are there any cultural or religious considerations that should be integrated into the design? (Select all that apply)',
      options: [
        'A. Prayer Room',
        'B. Cultural Symbolism',
        'C. Meditation Space',
        'D. Traditional Artifacts',
      ],
    },
    {
      question_number: 3,
      key: 'budget_range',
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
      key: 'family_size',
      question: 'How many family members will be residing in the home?',
      options: ['A. 0', 'B. 1-3', 'C. 4 - 7', 'D. 8+'],
    },
    {
      question_number: 5,
      key: 'security_safety',
      question: 'Do you have any specific security or safety requirements for your home?',
      options: ['A. Security System', 'B. Childproofing', 'C. Both', 'D. None'],
    },
    {
      question_number: 6,
      key: 'outdoor_spaces',
      question:
        'Do you require any outdoor spaces like a garden, patio, or playground for children? (Select all that apply)',
      options: ['A. Garden', 'B. Patio', 'C. Playground', 'D. None'],
    },
    {
      question_number: 7,
      key: 'vehicles_parking',
      question:
        'How many vehicles do you own, and do you need a garage or parking spaces for them?',
      options: ['A. No', 'B. 1', 'C. 2', 'D. 3'],
    },
    {
      question_number: 8,
      key: 'budget_allocation',
      question:
        'How would you prioritize budget allocation across different aspects of the project?',
      options: ['A. Construction', 'B. Interior Finish', 'C. Landscaping', 'D. Equal allocation'],
    },
    {
      question_number: 9,
      key: 'home_space',
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
      key: 'atmosphere_ambiance',
      question:
        'How would you describe your desired atmosphere or ambiance for the interior and exterior spaces?',
      options: ['A. Cozy', 'B. Minimalist', 'C. Elegant', 'D. Modern'],
    },
    {
      question_number: 11,
      key: 'design_inspirations',
      question:
        "Are there any specific design inspirations, such as a favorite vacation destination or art movement, that you'd like to draw upon for interior design?",
      options: ['A. Color Picker', 'B. Vintage', 'C. Contemporary', 'D. Natural'],
    },
    {
      question_number: 12,
      key: 'smart_home_technology',
      question:
        'Are you open to incorporating smart home technology for automation and control of various home systems? (Select all that apply)',
      options: ['A. Security', 'B. Lighting', 'C. Entertainment', 'D. All of the above'],
    },
    {
      question_number: 13,
      key: 'weather_concerns',
      question:
        'Are there any weather-related concerns or considerations for your project, such as extreme temperatures or heavy rainfall during certain seasons?',
      options: ['A. Extreme Temperature', 'B. Heavy Raining', 'C. Both', 'D. None'],
    },
    {
      question_number: 14,
      key: 'construction_phasing',
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
    if (typeof this.state[key] === 'string') this.setState({ [key]: option });
    else this.state[key].push(option);
  };

  analyze = () => {
    console.log(this.state)
    const { step } = this.state;
    this.setState({
      step: 0,
    });
  };

  render() {
    const { step } = this.state;
    if(step==0)
      return <LoadingScreen />;
      
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
