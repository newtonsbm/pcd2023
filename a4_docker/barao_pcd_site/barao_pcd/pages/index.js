import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Curso de Programação Concorrente e Distribuída
        </h1>

        <p className={styles.description}>
          8 semestre - Curso de Graduação em Ciências da Computação do Centro Universitário Barão de Mauá - 2020 - Ribeirão Preto / SP
        </p>

        
      </main>

      <footer className={styles.footer}>
        <a href="https://nextjs.org/learn"> NextJS</a>
        <img src="/vercel.svg" alt="Vercel Logo" className={styles.logo} />
      </footer>
    </div>
  )
}
