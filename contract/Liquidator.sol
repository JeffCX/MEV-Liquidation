pragma solidity ^0.8.6;

import "./Interface.sol";

contract performLiquidationOnCompound {

   IERC20 public token;
   CErc20 public ctoken;
   Comptroller public comptroller = Comptroller(0x3d9819210A31b4961b30EF54bE2aeD79B9c9Cd3B);
   PriceFeed public priceFeed = PriceFeed(0x922018674c12a7F0D394ebEEf9B58F186CdE13c1);

    function settoken(address _token) public {
        token = IERC20(_token);
    }
    function setctoken(address _ctoken) public {
        ctoken = CErc20(_ctoken);
    }

    function closeFactor() external view returns (uint) {
        return comptroller.closeFactorMantissa();
    }

    function liquidationIncentive() external view returns (uint) {
        return comptroller.liquidationIncentiveMantissa();
    }

    function amountToBeLiquidatedSieze(address _cToken, address _cTokenCollateral, uint _actualRepayAmount) external view returns (uint) {
        (uint error, uint cTokenCollateralAmount) = comptroller
        .liquidateCalculateSeizeTokens(
        _cToken,
        _cTokenCollateral,
        _actualRepayAmount
        );
        require(error == 0, "error");
        return cTokenCollateralAmount;
    }
 
    function liquidate(address _borrower, uint _repayAmount, address _cTokenCollateral) external {
        token.transferFrom(msg.sender, address(this), _repayAmount);
        token.approve(address(ctoken), _repayAmount);
        require(ctoken.liquidateBorrow(_borrower, _repayAmount, _cTokenCollateral) == 0, "liquidation failed");
    }

    function getPriceFeed(address _ctoken) external view returns (uint) {
        return priceFeed.getUnderlyingPrice(_ctoken);
    }

}