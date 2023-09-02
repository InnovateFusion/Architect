import { useEffect } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import { Box, Typography } from '@mui/material';

// ----------------------------------------------------------------------

export default function Index() {
  const router = useRouter();

  // useEffect(() => {
  //   if (router.pathname === '/') {
  //     router.push('/dashboard/one');
  //   }
  // });

  return (
    <>
      <Head>
        <title> Home </title>
      </Head>
      <Box
        sx={{
          display:'flex',
          justifyContent:'center',
          height:'100px'
        }
        }
      >
        <Typography>Wellcome to Home of Generative AI</Typography>
      </Box>
    </>
  );
}
