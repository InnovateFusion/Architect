import { Accordion, AccordionDetails, AccordionSummary, AppBar, Box, Dialog } from '@mui/material';
import React, { Component } from 'react';
import LoadingScreen from '../../components/loading-screen/LoadingScreen';
import Question from './question';
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
import CompactLayout from '../../layouts/compact';
// components
import { MotionContainer, varBounce } from '../../components/animate';
// assets
import { PageNotFoundIllustration } from '../../assets/illustrations';
import Iconify from 'src/components/iconify/Iconify';
import Block from 'src/components/settings/drawer/Block';
import Header from 'src/layouts/compact/Header';

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

export default function ResultForm({ response }) {
  return (
    <Block
      title="Select one"
      sx={{
        y: 5,
        m: 10,
      }}
    >
      <Header isOffset />
      <Accordion>
        <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
          <Typography variant="h3">Home Appearance</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <li>Features: {response.home_appearance.architectural_features}</li>
          <li>Interior style: {response.home_appearance.interior_style}</li>
          <li>Exterior style: {response.home_appearance.exterior_style}</li>
          <li>Color pallet: {response.home_appearance.color_palette}</li>
          <li>Number of Rooms: {response.home_appearance.numberOfclass}</li>
          <li>Number of Floors: {response.home_appearance.numberOffloor}</li>
        </AccordionDetails>
      </Accordion>
      <Accordion>
        <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
          <Typography variant="h3">Budget Analysis</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography variant="h4">
            Estimated Budget Needed: {response.budget_analysis.estimated_budget}
          </Typography>
          {response.budget_analysis.budget_allocation.map((v, i) => (
            <li key={i}>{v}</li>
          ))}
          <li>{response.budget_analysis.suggested_changes}</li>
          <Typography variant="h4">Detailed material cost:</Typography>
          {response.budget_analysis.detailed_material_costs.map((v, i) => (
            <li>{v}</li>
          ))}
          <li>Labour Cost: {response.budget_analysis.labor_costs}</li>
        </AccordionDetails>
      </Accordion>
      <Accordion>
        <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
          <Typography variant="h3">Timeline Analysis</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography variant="h4">
            Estimated Time Needed: {response.timeline_analysis.estimated_timeline}
          </Typography>
          <li>{response.timeline_analysis.phasing_details.description}</li>
          {response.timeline_analysis.phasing_details.phases.map((v, i) => (
            <li key={i}>{v}</li>
          ))}
        </AccordionDetails>
      </Accordion>
      <Accordion>
        <AccordionSummary expandIcon={<Iconify icon="eva:arrow-ios-downward-fill" />}>
          <Typography variant="h3">Recommendations</Typography>
        </AccordionSummary>
        <AccordionDetails>
          {response.recommendations.map((v, i) => (
            <li key={i}>{v}</li>
          ))}
        </AccordionDetails>
      </Accordion>
    </Block>
  );
}
