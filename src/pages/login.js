// next
import Head from 'next/head';
// auth
import GuestGuard from '../auth/GuestGuard';
// sections
import Login from '../sections/auth/Login';

// ----------------------------------------------------------------------

export default function LoginPage() {
  return (
    <>
      <Head>
        <title> Login | The Architect</title>
      </Head>

      <GuestGuard>
        R<Login />
      </GuestGuard>
    </>
  );
}
