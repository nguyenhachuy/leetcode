class RubyTest
    def initialize
        @variable_1 = 2
    end

    def print_variables
        puts @variable_1
    end
end

instance = RubyTest.new
instance.print_variables
