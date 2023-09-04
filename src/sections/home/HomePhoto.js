import { m } from 'framer-motion';
// @mui
import { alpha, styled } from '@mui/material/styles';
import { Box, Card, Container, Typography, Stack } from '@mui/material';
// components
import Image from '../../components/image';
import { MotionViewport, varFade } from '../../components/animate';

// ----------------------------------------------------------------------

const StyledRoot = styled('div')(({ theme }) => ({
  padding: theme.spacing(10, 0),
  [theme.breakpoints.up('md')]: {
    padding: theme.spacing(15, 0),
  },
}));

const StyledCard = styled(Card)(({ theme }) => ({
  backgroundColor: theme.palette.background.default,
  textAlign: 'center',
  padding: theme.spacing(10, 5),
  [theme.breakpoints.up('md')]: {
    boxShadow: 'none',
  },
}));

// ----------------------------------------------------------------------

export default function HomeMinimal() {
  return (
    <StyledRoot>
      <Container component={MotionViewport}>
        <Stack
          spacing={3}
          sx={{
            textAlign: 'center',
            mb: { xs: 2, md: 5 },
          }}
        >
          <m.div variants={varFade().inUp}>
            <Typography component="div" variant="overline" sx={{ color: 'text.disabled' }}>
              The Architect Produces
            </Typography>
          </m.div>

          <m.div variants={varFade().inDown}>
            <Typography variant="h2">
              Impresive Designs
            </Typography>
          </m.div>
        </Stack>

        <Box>
          <Box
            sx={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              overflow: 'hidden',
            }}
          >
            <img
              width="853"
              height="480"
              src="https://archccess.com/wp-content/uploads/2023/01/Midjourney-AI-generated-image.jpg"
              alt="this is a placeholder"
            />
          </Box>
        </Box>
      </Container>
    </StyledRoot>
  );
}
