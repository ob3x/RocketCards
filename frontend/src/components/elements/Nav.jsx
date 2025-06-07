import { Link } from 'react-router-dom';
import { logoWhiteImg } from '../../utils';

const Nav = () => {
  return (
    <nav className="fixed top-0 w-full p-10 sm:p-20 bg-blue-600 z-10">
      <div className="flex justify-between screen-max-width items-center">
        <Link to="/RocketCards" className="flex items-center">
          <span className="text-xs sm:text-xl text-white tracking-wider font-bold">RocketCards</span>
          <img src={logoWhiteImg} alt="logo" className="w-20 md:w-30 mx-2 md:mx-10 hidden sm:inline"/>
        </Link>
        <div>
          <Link to="/login" className="tracking-wider text-xs md:text-base font-bold mx-4 md:mx-20">
            <button className="button-class hover:button-class_hover px-5 sm:px-25">zaloguj się</button>
          </Link>
          <Link to="/register" className="tracking-wider text-xs md:text-base font-bold">
            <button className="button-class second-button hover:second-button_hover px-5 sm:px-25">stwórz konto</button>
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
