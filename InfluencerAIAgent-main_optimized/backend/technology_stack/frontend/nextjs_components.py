// Importing shared dependencies
// Importing components
const HomePage = () => {
const router = useRouter()
return (
<div>
<Head>
<title>AI Agent System for Influencers</title>
<link rel="icon" href="/favicon.ico" />
</Head>
<main>
<Profile userProfile={userProfile} />
<BrandCollaborations brandCollaborations={brandCollaborations} />
<ContentIdeas contentIdeas={contentIdeas} />
<PressReleases pressReleases={pressReleases} />
<LegalAdvice legalAdvice={legalAdvice} />
<ContactDatabase contactDatabase={contactDatabase} />
<AppointmentSchedule appointmentSchedule={appointmentSchedule} />
<StrategyInsights strategyInsights={strategyInsights} />
<PostPerformance postPerformance={postPerformance} />
<ApiIntegrations apiIntegrations={apiIntegrations} />
</main>
<footer>
<p>© 2022 Dr. A. I. Virtuoso</p>
</footer>
</div>
)
}
export default HomePage