import { m } from 'framer-motion';
// next
import Head from 'next/head';
import NextLink from 'next/link';
// @mui
import {
  Box,
  Button,
  Card,
  CardActionArea,
  CardContent,
  CardMedia,
  Grid,
  TextField,
  Typography,
} from '@mui/material';
// layouts
import CompactLayout from '../../layouts/compact';
// components
import { MotionContainer, varBounce } from '../../components/animate';
// assets
import { PageNotFoundIllustration } from '../../assets/illustrations';
import { random } from 'lodash';

// -----------------------MotionContainer-----------------------------------------------

Question.getLayout = (page) => <CompactLayout>{page}</CompactLayout>;

// ----------------------------------------------------------------------

export default function Question({ analyze, keyss, question, options, nextStep, handleChange }) {

  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        minHeight: 400,
        p: 10,
      }}
    >
      <MotionContainer>
        <m.div variants={varBounce().in}>
          <Typography variant="h4" paragraph>
            {question}
          </Typography>
        </m.div>
        <Grid
          container
          display='flex'
          justifyContent="center"
          sx={{
            textAlign: 'center',
          }}
        >
          {keyss !== 'interest' ? (
            options.map((option, index) => (
              <Grid
                item
                xs={12}
                md={6}
                gap={20}
                sx={{ mb: 3, display: 'flex', justifyContent: 'center', alignItems: 'center' }}
              >
                <m.div variants={varBounce().in}>
                  <Card>
                    <CardActionArea
                      sx={{
                        maxWidth: 375,
                        background: 'rgb(0,0,0,0.08)',
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'center',
                        textAlign: 'center',
                      }}
                      onClick={(e) => {
                        handleChange(keyss, option);
                      }}
                    >
                      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
                        <CardContent sx={{ width: 150 }}>{option}</CardContent>
                      </Box>
                      <CardMedia
                        component="img"
                        width={160}
                        height={160}
                        image={`/assets/images/rooms/room_${index + random(1, 2)}.jpg`}
                      />
                    </CardActionArea>
                  </Card>
                </m.div>
              </Grid>
            ))
          ) : (
            <TextField
              onChange={(e) => {
                handleChange(keyss, e.target.value);
              }}
              fullWidth
              label="optional"
              id="fullWidth"
              multiline
              rows={3}
              sx={{ m: 3 }}
            />
          )}
        </Grid>

        {/* <m.div variants={varBounce().in}>
          <PageNotFoundIllustration
            sx={{
              height: 60,
              my: { xs: 5, sm: 10 },
            }}
          />
        </m.div> */}

        <Button
          sx={{ float: 'right', mb: 2 }}
          onClick={keyss === 'interest' ? analyze : nextStep}
          size="large"
          variant="contained"
        >
          {keyss === 'interest' ? 'Generate' : 'Next'}
        </Button>
      </MotionContainer>
    </Box>
  );
}
