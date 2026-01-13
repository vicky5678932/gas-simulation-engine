import random

def simulate_tx_execution(gas_limit, gas_price_gwei, complexity=1.0):
    """
    Simulates transaction execution and returns estimated actual usage.
    """
    # Base usage is usually around 21k for simple transfers
    base_usage = 21000
    
    # Calculate variable usage based on complexity
    # Complexity 1.0 = simple transfer, >1.0 = smart contract interaction
    variable_usage = (gas_limit - base_usage) * complexity
    
    # Add some randomness for network conditions / contract state
    efficiency_factor = random.uniform(0.85, 0.98)
    actual_usage = base_usage + (variable_usage * efficiency_factor)
    
    # Final cost in ETH
    cost_eth = (actual_usage * gas_price_gwei) / 1e9
    
    return {
        "actual_usage": int(actual_usage),
        "cost_eth": round(cost_eth, 6),
        "success": actual_usage <= gas_limit
    }

if __name__ == "__main__":
    # Test simulation
    res = simulate_tx_execution(100000, 30, complexity=1.5)
    print(f"Simulation result: {res}")
