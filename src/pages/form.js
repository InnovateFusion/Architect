import { Accordion, AccordionDetails, AccordionSummary, AppBar, Box, Dialog } from '@mui/material';
import React, { Component } from 'react';
import LoadingScreen from '../components/loading-screen/LoadingScreen';
import Question from '../sections/demo/question';
// import FormUserDetails from './FormUserDetails';
// import FormPersonalDetails from './FormPersonalDetails';
// import Confirm from './Confirm';
// import Success from './Success';
import { m } from 'framer-motion';
// next
import Head from 'next/head';
import NextLink from 'next/link';
// @mui
import { Button, Typography } from '@mui/material';
// layouts
import CompactLayout from '../layouts/compact';
// components
import { MotionContainer, varBounce } from '../components/animate';
// assets
import { PageNotFoundIllustration } from '../assets/illustrations';
import Iconify from 'src/components/iconify/Iconify';
import Block from 'src/components/settings/drawer/Block';

const response = {
  status: 'success',
  feasibility: 'yes',
  home_appearance: {
    interior_style: 'Cozy',
    exterior_style: 'Vintage',
    color_palette: 'Warm Tones',
    architectural_features: 'Traditional design with ornate details and elements',
    numberOfclass: '4',
    numberOffloor: '2',
  },
  budget_analysis: {
    estimated_budget: '$300,000',
    budget_allocation: [
      'Construction: $100,000',
      'Interior Finish: $90,000',
      'Landscaping: $60,000',
      'Equal allocation: $50,000',
    ],
    suggested_changes: '',
    detailed_material_costs: ['steel_bar: $30,000', 'concrete: $50,000', 'wood: $60,000', 'others'],
    labor_costs: '$100,000',
  },
  timeline_analysis: {
    estimated_timeline: '18 months',
    phasing_details: {
      description: 'The project can be divided into 6 phases for 6 occupations.',
      phases: [
        'Phase 1: Foundation and framing',
        'Phase 2: Roofing and exterior walls',
        'Phase 3: Interior walls and flooring',
        'Phase 4: Electrical and plumbing',
        'Phase 5: Interior finishes',
        'Phase 6: Landscaping and final touches',
      ],
    },
  },
  recommendations: [
    'Consider incorporating energy-efficient features and materials for long-term cost savings.',
    'Explore options for integrating smart home technology for convenience and control.',
  ],
};



 
export class UserForm extends Component {
  render() {
    return (
      <Block
        title="Select one"
        sx={{
          y: 5,
          m: 10,
        }}
      >
        <Accordion>
          <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
            <Typography variant="subtitle1">Home Appearance</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <li>{response.home_appearance.architectural_features}</li>
            <li>{response.home_appearance.interior_style}</li>
            <li>{response.home_appearance.exterior_style}</li>
            <li>{response.home_appearance.color_palette}</li>
            <li>{response.home_appearance.numberOfclass}</li>
            <li>{response.home_appearance.numberOffloor}</li>
          </AccordionDetails>
        </Accordion>
        <Accordion>
          <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
            <Typography variant="subtitle1">Budget Analysis</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {response.home_appearance.architectural_features}
            <Typography>{'accordion.detail'}</Typography>
          </AccordionDetails>
        </Accordion>
        <Accordion>
          <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
            <Typography variant="subtitle1">Timeline Analysis</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {response.home_appearance.architectural_features}
            <Typography>{'accordion.detail'}</Typography>
          </AccordionDetails>
        </Accordion>
        <Accordion>
          <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
            <Typography variant="subtitle1">Recommendations</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {response.home_appearance.architectural_features}
            <Typography>{'accordion.detail'}</Typography>
          </AccordionDetails>
        </Accordion>
      </Block>
    );


    return (
      <MotionContainer>
        <m.div variants={varBounce().in}>
          <Typography variant="h3" paragraph>
            Sorry, page not found!
          </Typography>
        </m.div>

        <m.div variants={varBounce().in}>
          <Typography sx={{ color: 'text.secondary' }}>
            Sorry, we couldn’t find the page you’re looking for. Perhaps you’ve mistyped the URL? Be
            sure to check your spelling.
          </Typography>
        </m.div>

        <m.div variants={varBounce().in}>
          <PageNotFoundIllustration
            sx={{
              height: 260,
              my: { xs: 5, sm: 10 },
            }}
          />
        </m.div>

        <Button component={NextLink} href="/" size="large" variant="contained">
          Go to Home
        </Button>
      </MotionContainer>
    );
  }
}

// UserForm.getLayout = (page) => <CompactLayout>{page}</CompactLayout>;
export default UserForm;
