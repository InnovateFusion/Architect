import { m } from 'framer-motion';
// @mui
import { alpha, styled } from '@mui/material/styles';
import { Box, Card, Container, Typography, Stack } from '@mui/material';
// components
import Image from '../../components/image';
import { MotionViewport, varFade } from '../../components/animate';

// ----------------------------------------------------------------------

const CARDS = [
  {
    icon: ' /assets/icons/home/ic_make_brand.svg',
    title: 'Branding',
    description: 'Consistent design makes it easy to brand your own.',
  },
  {
    icon: ' /assets/icons/home/ic_design.svg',
    title: 'UI & UX Design',
    description:
      'The kit is built on the principles of the atomic design system. It helps you to create projects fastest and easily customized packages for your projects.',
  },
  {
    icon: ' /assets/icons/home/ic_development.svg',
    title: 'Development',
    description: 'Easy to customize and extend, saving you time and money.',
  },
];

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

export default function HomeAI() {
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
              Easy Communication
            </Typography>
          </m.div>

          <m.div variants={varFade().inDown}>
            <Typography variant="h2">
              Artificial Intelligence <br /> Assistant
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
            <iframe
              width="953"
              height="580"
              src="https://talking-avatar-ten.vercel.app"
              title="The Architect"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowFullScreen
            />
          </Box>
        </Box>
      </Container>
    </StyledRoot>
  );
}
