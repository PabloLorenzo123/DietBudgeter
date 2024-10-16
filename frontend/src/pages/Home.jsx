
import '../styles/home.css';

const Home = () => {

    return(
        <>
            <div className="main-nav">
                <div className="main-nav-left">
                    <h1>DietBudgeter</h1>
                </div>
                <div className="main-nav-right">
                    <nav>
                        <ul>
                            <a href="#about-us">
                                <li>
                                    About
                                </li>
                            </a>
                            <a href="/login/">
                                <li className="nav-button">
                                    LOG IN
                                </li>
                            </a>
                        </ul>
                    </nav>
                </div>
            </div>

            <div id="hero">
                <h1>
                    Eat smarter.
                    <br/>
                    Save more.
                </h1>
                <h5>Plan your diet, hit your nutrient goals without breaking the bank.</h5>
                
                <a href="signup/">
                    <button>
                        Sign Up
                    </button>
                </a>
            </div>
            
        </>
    )
}

export default Home