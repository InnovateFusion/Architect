import { Accordion, AccordionDetails, AccordionSummary, AppBar, Box, Dialog } from '@mui/material';
import React, { Component, useEffect, useState } from 'react';
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
import axiosInstance from 'src/utils/axios';
import Image from 'src/components/image/Image';

const Images = [
  'https://res.cloudinary.com/dtghsmx0s/image/upload/v1693751132/u1fzsnehmzr2cvk34e7h.png',
  'http://res.cloudinary.com/dtghsmx0s/image/upload/v1693751134/zmns7rzonxeht9tw4kgq.jpg',
  'https://res.cloudinary.com/dtghsmx0s/image/upload/v1693759764/undjrkq5fttpps5tutyz.png',
];

export default function ResultForm({ response, homeid = 'eb553069-fec1-4018-a5d3-a76713d420ed' }) {
  return (
    <Block
      title="Select one"
      sx={{
        y: 5,
        m: 10,
      }}
    >
      <Header isOffset />
      <Box sx={{ display: 'flex', flexDirection:'row', justifyContent:'space-evenly' }}>
        <Image disabledEffect visibleByDefault alt="auth" src={Images[0]} sx={{ maxWidth: 520 }} />
        <Image disabledEffect visibleByDefault alt="auth" src={Images[2]} sx={{ maxWidth: 520 }} />
      </Box>
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
            <li key={i}>{v}</li>
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
